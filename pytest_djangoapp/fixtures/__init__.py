# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from .request import request_factory, request_get
from .settings import settings
from .templates import template_render_tag, template_context, template_strip_tags
from .users import user_create, user_model

fixtures_registered = True
