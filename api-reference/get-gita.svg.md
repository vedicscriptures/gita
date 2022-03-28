---
description: GET random or perticular slok Image of Shreemad Bhagavad Gita
---

# GET /gita.svg

{% swagger baseUrl="https://bhagavadgitaapi.in" path="/gita.svg" method="get" summary="/gita.svg" %}
{% swagger-description %}
This endpoint allows you to get any random or perticular slok Image of Shreemad Bhagavad Gita
{% endswagger-description %}

{% swagger-parameter in="query" name="ch" type="integer" %}
specfic chapter number from any of 18 chapters
{% endswagger-parameter %}

{% swagger-parameter in="query" name="sl" type="integer" %}
specfic slok number avilable in taht particuler
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}

{% swagger-response status="404" description="Could not find a matching this query." %}
```
{ error: 'Internal Server Error'}
```
{% endswagger-response %}
{% endswagger %}

{% hint style="success" %}
response (200 ok)
{% endhint %}

![shrimad bhagwat geeta adhyay 1 shlok 1](../.gitbook/assets/gita.svg)
