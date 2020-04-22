<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
	<UL>
	    {% for state in states.values() | sort(attribute="name") %}
	    <LI>{{ state.id }} <B>{{ state.name }}</B>
                <UL>
                    {% for city in cities.values() | sort(attribute="name") %}
                        {% if city.state_id == state.id %}
                        <LI>{{ city.id}} <B>{{ city.name }}></B></LI>
                        {% endif %}
                    {% endfor %}
                <UL>
            </LI>
            {% endfor %}
	</UL>
    </BODY>
</HTML>
