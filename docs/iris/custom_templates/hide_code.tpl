{% extends 'html.tpl' %}

{% block input %}
    {% if cell['metadata'].get('skip', False) %}
        {% else %}
        <div class="input">
            {{ super() }}
        </div>
    {% endif %}
{% endblock %}