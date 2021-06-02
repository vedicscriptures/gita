---
description: GET random or perticular slok Image of Shreemad Bhagavad Gita
---
# GET /gita.svg

{% api-method method="get" host="https://bhagavadgitaapi.in" path="/gita.svg" %}
{% api-method-summary %}
/gita.svg
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to get any random or perticular slok Image of Shreemad Bhagavad Gita
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="x-api-key" type="string" required=false %}
Authentication token to track down who is emptying our stocks.
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-query-parameters %}
{% api-method-parameter type="string" name="api\_key" %}
Alternate way to send Authentication token
{% endapi-method-parameter %}
{% api-method-parameter type="integer" name="chapter\_num" %}
specfic chapter number from any of 18 chapters
{% endapi-method-parameter %}
{% api-method-parameter type="integer" name="slok\_num" %}
specfic slok number avilable in taht particuler
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
successfully retrieved.
{% endapi-method-response-example-description %}
{% endapi-method-response-example %}
![](https://instagram.fidr3-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/129738801_403477617629742_1762660810707419049_n.jpg?tp=1&_nc_ht=instagram.fidr3-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=uN_39EIFJ_oAX9D-IL7&edm=AP_V10EBAAAA&ccb=7-4&oh=3d31cbb9305a16d057d0f928522db038&oe=60BD4663&_nc_sid=4f375e)

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Could not find a matching this query.
{% endapi-method-response-example-description %}

```text
{ error: 'Internal Server Error'}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

