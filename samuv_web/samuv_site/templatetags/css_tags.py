from django import template

register = template.Library()

@register.filter(name='add_css')
def add_css(field, css):
	class_old = field.field.widget.attrs.get('class', None)
	class_new = class_old + ' ' + css if class_old else css
	return field.as_widget(attrs={"class": class_new})

@register.filter(name='add_css_text')
def add_css(field, css):
	print(field, css)
	old_class = field.field.CharField('class', None)
	new_class = old_class + ' ' + css if old_class else css
	return field.as_widget(attrs={'class': new_class})

@register.filter(name='add_css_date')
def add_css(field, css):
	print(field, css)
	old_class = field.field.DateTimeField('class', None)
	new_class = old_class + ' ' + css if old_class else css
	return field.as_widget(attrs={'class': new_class})
