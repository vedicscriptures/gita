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

{% hint style="success" %}
response \(200 ok\)
{% endhint %}

![shrimad bhagwat geeta adhyay 1 shlok 1](../.gitbook/assets/gita.svg)

