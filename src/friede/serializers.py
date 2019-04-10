# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer,\
    HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework_recursive.fields import RecursiveField
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin
from collections import OrderedDict

from .models import *

class F:
    _base = ( 'url', 'id', 'name', 'title', 'description', 'active', 'path' )
    base = ( 'url', 'id', 'name', 'title', 'description', 'active', 'icon', 'path' )
    entries = ( '_container_entries', '_widget_entries', '_block_entries',
                '_screen_entries', '_shell_entries', '_theme_entries', '_slot_entries',
                '_app_entries', '_location_entries', '_icon_entries', '_link_entries',
                '_reference_entries', '_setting_entries' )
    # entries = tuple()
    extends = ( 'extends', )
    size = ( 'min_x', 'min_y', 'max_x', 'max_y' )
    data = ( 'data', )
    templates = ( 'templates', 'template' )
    app = ( 'module', 'rest', 'version' )
    location = ( 'href', 'redirect_to' )
    link = ( 'location', )
    reference = ( 'target', )
    setting = ( 'type', 'default' )
    entry = ( 'url', 'id', 'name', 'title', 'description', 'active', 'icon', 'name', )
    # ( 'entry', 'position' )


class EntrySerializer( ModelSerializer ):
    pass

class ContainerEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='containerentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = ContainerEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.ContainerSerializer'
        )

class WidgetEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='widgetentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = WidgetEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.WidgetSerializer'
        )


class BlockEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='blockentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = BlockEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.BlockSerializer'
        )


class ScreenEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='screenentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = ScreenEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.ScreenSerializer'
        )


class ShellEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='shellentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = ShellEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.ShellSerializer'
        )


class ThemeEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='themeentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = ThemeEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.ThemeSerializer'
        )


class SlotEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='slotentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = SlotEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.SlotSerializer'
        )


class AppEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='appentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = AppEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.AppSerializer'
        )


class LocationEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='locationentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = LocationEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.LocationSerializer'
        )


class IconEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='iconentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = IconEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.IconSerializer'
        )


class LinkEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='linkentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = LinkEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.LinkSerializer'
        )


class ReferenceEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='referenceentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = ReferenceEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.ReferenceSerializer'
        )


class SettingEntrySerializer( EntrySerializer ):
    url = HyperlinkedIdentityField( view_name='settingentry-detail',
                                    lookup_field='registry' )
    class Meta:
        model = SettingEntry
        fields = F.entry
        expanded_fields = OrderedDict(
            registry='friede.serializers.RegistrySerializer',
            entry='friede.serializers.SettingSerializer'
        )


class RegistrySerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    _container_entries = ContainerEntrySerializer()
    _widget_entries =    WidgetEntrySerializer()
    _block_entries =     BlockEntrySerializer()
    _screen_entries =    ScreenEntrySerializer()
    _shell_entries =     ShellEntrySerializer()
    _theme_entries =     ThemeEntrySerializer()
    _slot_entries =      SlotEntrySerializer()
    _app_entries =       AppEntrySerializer()
    _location_entries =  LocationEntrySerializer()
    _icon_entries =      IconEntrySerializer()
    _link_entries =      LinkEntrySerializer()
    _reference_entries = ReferenceEntrySerializer()
    _setting_entries =   SettingEntrySerializer()
    class Meta:
        model = Registry
        fields = F.base + F.entries


class ContainerSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Container
        fields = F.base + F.entries


class WidgetSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Widget
        fields = F.base + F.entries + F.extends + F.size + F.data


class BlockSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Block
        fields = F.base + F.entries + F.extends + F.size + F.data


class ScreenSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Screen
        fields = F.base + F.entries + F.extends + F.size + F.data


class ShellSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Shell
        fields = F.base + F.entries + F.extends + F.templates


class ThemeSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Theme
        fields = F.base + F.entries + F.extends + F.templates


class SlotSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = Slot
        fields = F.base + F.entries


class AppSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    class Meta:
        model = App
        fields = F.base + F.entries + F.data + F.app


class LocationSerializer( SerializerExtensionsMixin, HyperlinkedModelSerializer ):
    redirect_to = RecursiveField( allow_null=True )
    class Meta:
        model = Location
        fields = F.base + F.entries + F.data + F.location


class IconSerializer( HyperlinkedModelSerializer ):
    class Meta:
        model = Icon
        fields = F._base


class LinkSerializer( HyperlinkedModelSerializer ):
    class Meta:
        model = Link
        fields = F.base + F.entries + F.location


class ReferenceSerializer( HyperlinkedModelSerializer ):
    class Meta:
        model = Reference
        fields = F.base + F.entries + F.reference


class SettingSerializer( HyperlinkedModelSerializer ):
    class Meta:
        model = Setting
        fields = F.base + F.data + F.setting


