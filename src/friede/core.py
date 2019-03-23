# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .objects import Settings, Shells, getenv, getregistries, getshell
from .models import Setting, Shell, Theme, ShellEntry, ThemeEntry
from django.core.exceptions import ObjectDoesNotExist

def setup():
    "make new settings"
    # settings = Settings()
    # shell_setting = settings.sys.ui.shell.get_or_create(
    #     type=Setting.Types.Choice,
    #     data=dict(
    #         model='Shell',
    #         registry__parent__name=''
    #     ))
    # maybe not yet
    env = getenv()
    shell = env.H.current
    if not shell:
        shell = Shells().mayflower.get()
        if not shell:
            shell = setupshell( env )

def setupshell( env=None ):
    "make (and select) the default shell"
    if not env:
        env = getenv()
    shell = None
    try:
        shell = Shell.objects.get( path='shells.mayflower' )
    except:
        shell = Shell.objects.create(
            path='shells.mayflower',
            templates='friede/mayflower'
        )
    env.addshell( 'current', shell )
    setuptheme( shell )
    return shell

def setuptheme( shell=None ):
    "make (and select) the default theme for the current shell"
    if not shell:
        shell = Shells().mayflower.get()
    theme = None
    try:
        theme = Theme.objects.get( path='themes.acamar' )
    except ObjectDoesNotExist:
        theme = Theme.objects.create(
            name='themes.acamar',
            templates='friede/mayflower/acamar'
        )
    shell.addtheme( 'current', theme )
    return theme