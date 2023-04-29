from django import template
from ..models import Category
from django.shortcuts import get_list_or_404

register = template.Library()


# @register.simple_tag
# def title(data):
# 	return str(data).split(',')
from django.db.models.fields.files import FileField
import re
@register.filter
def images_address(data):
	url_pattern = r'^(.*[\\\/])[^\\\/]*$'
	image_pattern = r'([^\/]+$)'
	# image = re.split(image_pattern, str(data.url), maxsplit=5)
	url = re.findall(url_pattern, data.url)[0]
	images = [list(map(lambda img: url + img, str(item.group()).split('%2C'))) for item in re.finditer(image_pattern, data.url)][0]
	print(url)
	return images
