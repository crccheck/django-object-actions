/*
{% comment %}

So admin/change_form.html doesn't have the right block names to make inserting
new list items easy. So insert our list items somewhere close to where they are
supposed to show up and then move them with magic.

If you need special logic because you're using a custom skin like admin-tools,
override this file using template inheritance.

So in case you didn't get it by now, this is inserted with an include tag, not
admin staticfiles.

{% endcomment %}
*/
/* global: $ */
$('li.objectaction-item').prependTo($('#content-main ul.object-tools'));
