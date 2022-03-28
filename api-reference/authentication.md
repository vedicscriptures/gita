---
description: >-
  If you don’t have an API Key, just head over to
  https://bhagavadgitaapi.in/pricing and get one for free
---

# Authentication

* Use the API Key that was **emailed** to you when you signed up to authenticate every request you send to the API.
* Without it you only have access to a tiny amount of data in a random order, and cannot upload, vote or favourite.
* You can send your API Key as a header or a query parameter

{% hint style="info" %}
if you don’t have an API Key, just head over to [https://bhagavadgitaapi.in/pricing](https://bhagavadgitaapi.in/pricing) and get one for free
{% endhint %}

## Request Header

* The best & most secure way to send it
* Set your API Key as the **x-api-key** header on evey request.
* * e.g **headers\[“x-api-key”\] = "ABC123"**

## Query Parameter

* The least secure way, and not advisable unless there is no other way.
* Intended for use in IoT use-cases & backwards compatibility
* Pass as the **api\_key** query parameter

{% hint style="info" %}
e.g. [https://bhagavadgitaapi.in/gita?api\_key=ABC123](https://bhagavadgitaapi.in/gita?**api_key=ABC123**)
{% endhint %}

