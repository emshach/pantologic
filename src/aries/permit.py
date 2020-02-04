# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from importlib import import_module
from packaging.version import parse as version_parse
from django.conf import settings
from collections import OrderedDict, deque
from django.db import transaction
from django.db.models import Model
from django.contrib.contenttypes.models import ContentType
from . import models as M
import traceback
import sys

rules = []
permits = OrderedDict()

def setup():
    from . import aries_permit
    try:
        permits[ 'aries' ] = aries_permit.Permit()
        for app_name in settings.INSTALLED_APPS:
            if app_name == 'aries': continue
            name = app_name
            module = app_name
            if module:
                try:
                    permit = import_module( "%s.aries_permit" % module )
                    permits[ module ] = permit.Permit()
                except ( ImportError, AttributeError ) as e:
                    msg = str(e)
                    if 'No module named aries_permit' not in msg:
                        print >> sys.stderr, 'got exception', type(e), e,\
                            "in aries.permit/%s" % module
                        traceback.print_exc()
                    continue        # TODO: maybe warn
    except Exception:
        # pass                        # TODO: handle
        raise

class Permit( object ):
    rules = ()
    data = ()
    model = None
    name = ''
    def __init__( self ):
        super( Permit, self ).__init__()
        self.model, _ = M.Permit.objects.get_or_create( name=self.name )
        self.installrules()
        self.installdata()

    def installrules( self ):
        rules.extend([ (r,) + ((),) if len(r) < 3 else r[:3] for r in self.rules ])

    def installdata( self ):
        version = self.version
        available = None
        error = None
        types = dict(
            users=M.User,
            groups=M.Group,
            roles=M.Role,
            permissions=M.Permission,
            policies=M.Policy,
        )
        names = dict(
            users=lambda x: '_'.join(x),
            groups=lambda x: '.'.join(x),
            roles=lambda x: '.'.join(x),
            permissions=lambda x: '_'.join(x),
            policies=lambda x: '.'.join(x),
        )
        namefields = dict(
            users='username',
            groups='name',
            roles='name',
            permissions='codename',
            policies='name',
        )
        def set_superuser( user ):
            user.is_superuser=True
            user.save()
        ops = dict(
            superuser=set_superuser
        )
        def update_version ():
            self.version = available

        for tree in self.data:
            v = version_parse( tree[0] )
            print 'installing', self.name, 'security permit', v
            available = v
            if error or v <= version:
                continue
            with transaction.atomic():
                transaction.on_commit( update_version )
                stack = deque([ tree[1:] ])
                name = deque([''])
                data = deque([ None ])
                model = deque([ None ])
                cr = deque([()])

                def mkobject( Type, name=None, data={}):
                    data = dict( data ) # copy
                    if not name:
                        if data.get( 'name' ):
                            if callable( data[ 'name' ]):
                                name = data['name']( name )
                            else:
                                name = data.pop( 'name' )
                    for k, v in data.items():
                        if callable(v):
                            data[k] = v( name, data )
                    tag = model[0]
                    if isinstance( name, ( tuple, list )):
                        name = names[ tag ]( name )
                    search = { namefields[ tag ]: name }
                    if tag == 'permissions' and 'ct' in data:
                        ct = data.pop( 'ct' )
                        if isinstance( ct, basestring ):
                            if '.' in ct:
                                app, mod = ct.split('.')
                                search[ 'content_type_id' ] = \
                                    ContentType.objects.get(
                                        app_label=app, model=mod ).id
                            elif ct in types:
                                search[ 'content_type_id' ] = \
                                    ContentType.objects.get_for_model(
                                        types[ ct ]).id
                            else:
                                raise KeyError( "no content type for '%s'" % ct )
                        elif hasattr( ct, '__class__' ) and issubclass( ct, Model ):
                            search[ 'content_type_id' ] = \
                                    ContentType.objects.get_for_model( ct ).id
                        else:
                            raise ValueError( "bad content-type: %s" % ct )
                    print 'uoc permission', data, search
                    obj, new = Type.objects.update_or_create( defaults=data, **search )
                    print 'created' if new else 'updated', Type._meta.model_name,\
                        name
                    return obj

                def mkobjects( attrs={} ):
                    if not model[0] or not data[0]:
                        return
                    cr[0] = tuple( map(
                        lambda x: mkobject( types[ model[0] ], x, attrs ),
                        data[0] ))
                    if len(cr) > 1:
                        objects = cr[0]
                        parents = cr[1]
                        if parents and objects:
                            tag = model[0]
                            rel = 'user_permissions' \
                                if tag == 'permissions' and model[1] == 'users' \
                                else tag
                            for p in parents:
                                getattr( p, rel ).add( *objects )
                                print 'added', objects, 'to', p

                def popstack():
                    stack.pop()

                def popmodel():
                    model.popleft()

                def popcr():
                    cr.popleft()

                def poperate():
                    mkobjects()
                    data.popleft()

                def popdata():
                    data.popleft()
                try:
                    while stack:
                        top = stack.pop()
                        if isinstance( top, tuple ):
                            if not len( top ):
                                continue
                            tag = top[0]
                            body = top[1:]
                            if isinstance( tag, basestring ):
                                if tag.startswith('#'):
                                    tag = tag[1:]
                                    if tag in ops:
                                        if not cr[0]: mkobjects()
                                        for obj in cr[0]:
                                            ops[ tag ]( obj )
                                    elif tag in types:
                                        model.appendleft( tag )
                                        cr.appendleft(())
                                        data.appendleft( None )
                                        stack.extend(( popdata, popmodel, popcr ))
                                        stack.extend( body[::-1] )
                                        continue
                                    else:
                                        raise NameError(
                                            "unknown instruction '#%s'" % tag )
                                else:
                                    tag = map( lambda x: (x,),
                                               filter( lambda x: x, tag.split()))
                            if isinstance( tag, list ):
                                items = tuple(
                                    x + y for x in data[0] for y in tag
                                ) if data[0] else tag
                                data.appendleft( items )
                                if len( body ):
                                    stack.append( popdata )
                                    if isinstance( body[0], basestring ):
                                        stack.append( body )
                                    else:
                                        stack.extend( body[ ::-1 ])
                                else:
                                    stack.append( poperate )
                            else:
                                # flatten tuples
                                stack.extend( top[ ::-1 ])
                        elif isinstance( top, list ):
                            stack.extend( tuple(( x, {} ) for x in top[ ::-1 ]))
                        elif isinstance( top, dict ):
                            mkobjects( top )
                        elif isinstance( top, basestring ):
                            stack.append(( top, ))
                        elif callable( top ):
                            top()
                except Exception as e:
                    print >> sys.stderr, "got exception", type(e), e
                    traceback.print_exc()
                    error = True
                    raise

        self.available = available

    @property
    def version( self ):
        return version_parse( self.model.version )

    @version.setter
    def version( self, version ):
        self.model.version = str( version )
        self.model.save()

    @property
    def available( self ):
        return version_parse( self.model.available )

    @available.setter
    def available( self, available ):
        self.model.available = str( available )
        self.model.save()

