<center><h1>Bhagavad Gita API</h1></center>
<p align="center"><img alt="Bhagavad Gita API" src="https://raw.githubusercontent.com/vedicscriptures/bhagavad-gita-api/main/docs/gita-logo.jpg" width="300vw"/></p>
<p align="center">
	<a href="https://github.com/PtPrashantTripathi"><img alt="Devloper" src="https://img.shields.io/badge/Devloper-Pt.%20Prashant%20Tripathi-Success.svg?style=flat-square"/></a>
	<a href="https://github.com/vedicscriptures/bhagavad-gita-api/LICENSE"><img alt="License" src="https://img.shields.io/github/license/vedicscriptures/bhagavad-gita-api.svg?style=flat-square"/></a>
	<a href="https://ptprashanttripathi.github.io"><img alt="Website Status" src="https://img.shields.io/website/http/ptprashanttripathi.github.io.svg?down_message=Down&up_message=Online&style=flat-square"/></a>
	<a href="https://github.com/vedicscriptures/bhagavad-gita-api/stargazers"><img alt="stars-shield" src="https://img.shields.io/github/stars/vedicscriptures/bhagavad-gita-api.svg?style=flat-square"/></a>
	<a href="https://github.com/vedicscriptures/bhagavad-gita-api/network/members"><img alt="forks-shield" src="https://img.shields.io/github/forks/vedicscriptures/bhagavad-gita-api.svg?style=flat-square"/></a>
	<a href="https://github.com/vedicscriptures/bhagavad-gita-api/graphs/traffic"><img alt="Total-Downlode" src="https://img.shields.io/github/downloads/vedicscriptures/bhagavad-gita-api/total.svg?style=flat-square"/></a>
</p>
<p align="center">
	<a href="https://ptprashanttripathi.github.io">View Demo</a> · <a href="https://github.com/PtPrashantTripathi/ptprashanttripathi.github.io/issues/new/choose">Report Bug</a> · <a href="https://github.com/PtPrashantTripathi/ptprashanttripathi.github.io/issues/new/choose">Request Feature</a>
</p>
<p align="center">
	<i>Loved the tool? Please consider <a href="https://paypal.me/ptprashanttripathi/100">donating</a> 💸 to help it improve!</i><br>
	<a href="https://paypal.me/PtPrashantTripathi"><img height='23' src="https://img.shields.io/badge/support-PayPal-blue?logo=PayPal&style=flat-square&label=Donate" alt="Donate"/></a>
	<a href='https://ko-fi.com/ptprashanttripathi' target='_blank'><img height='23' width="100" src='https://cdn.ko-fi.com/cdn/kofi3.png?v=2' alt='Buy Coffee for ptprashanttripathi' /></a>
	<a href="https://www.buymeacoffee.com/ptprashant09" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="23" width="100" style="border-radius:1px" /></a>
	<a href="https://ptprashanttripathi.github.io/linkpe?pa=pt1998@ybl&pn=Pt.+Prashant+Tripati" target="_blank"><img src="https://raw.githubusercontent.com/PtPrashantTripathi/linkpe/main/img/linkpebadge.svg" alt="Support Via UPI" height="23" style="border-radius:1px" /></a>
</p>

## About

Bhagavad-Gita-API is A lightweight Node.js based Bhagavad Gita API server 

## 🚀 How to use

### 1. Homepage

- **`URL`**  : `https://vedicscripturesapi.herokuapp.com/`

### 2. GET SVG of Random Slok of Shreemad Bhagavad Gita

- **`URL`**  : `https://vedicscripturesapi.herokuapp.com/gita.svg`
- **`Method`** : `GET`

#### Success Response

- **`Response Code`** : `200`
- **`Content example (SVG)`**

![bhagavad Gita img example](https://vedicscripturesapi.herokuapp.com/gita.svg)

### 3. GET SVG of Randome Slok from Particuler chapter of Shreemad Bhagavad Gita

- **`URL`** : `https://vedicscripturesapi.herokuapp.com/gita.svg?ch={chapter num}`
- **`Method`** : `GET` 
- **`{Chapter num}`** : `[interger]` specfic chapter number from any of 18 chapters 

#### Success Response

- **`Condition`** : if chapter num is correct.
- **`Response Code`** : `200`
- **`Content example (SVG)`**

![bhagavad Gita img example](https://vedicscripturesapi.herokuapp.com/gita.svg?ch=1)

#### Error Response

- **`Condition`** : if chapter num number conatan wrong value
- **`Response Code`** : `400`
- **`Content example-`**

``json
{ "error" : "" }
``

### 4. GET SVG of Slok from Particuler slok & chapter of Shreemad Bhagavad Gita

- **`URL`** : `https://vedicscripturesapi.herokuapp.com/gita.svg?ch={chapter num}&sl={slok num}`
- **`Method`** : `GET` 
- **`Chapter num`** : `[interger]` specfic chapter number from any of 18 chapters 
- **`Slok num`** : `[interger]` specfic slok number avilable in taht particuler `chapter` 

#### Success Response

- **`Condition`** : if chapter and slok num is correct.
- **`Response Code`** : `200`
- **`Content example (SVG)`**

![bhagavad Gita img example](https://vedicscripturesapi.herokuapp.com/gita.svg?ch=1&sl=1)

#### Error Response

- **`Condition`** : if chapter num or slok number conatan wrong value
- **`Response Code`** : `400`
- **`Content example`**

``json
{ "error" : "" }
``

### 5. GET Random gita Slok(Verse)

- **`URL`** : `https://vedicscripturesapi.herokuapp.com/gita`
- **`Method`** : `GET` 

#### Success Response

- **`Response Code`** : `200`
- **`Content example json`**

``json
{ "sajdsaio" : "" }
``

### 6. GET All Chapters details of Shreemad Bhagavad Gita

- **`URL`** : `https://vedicscripturesapi.herokuapp.com/gita/chapters`
- **`Method`** : `GET` 

#### Success Response

- **`Response Code`** : `200`
- **`Content example json`**

``json
{ "sajdsaio" : "" }
``

### 7. GET Particular Chapters details of Shreemad Bhagavad Gita

- **Endpoint** `https://vedicscripturesapi.herokuapp.com/gita{/:cp}`
- **`Method`** : `GET` 
- **`:ch`** : `[interger]` specfic chapter number from any of 18 chapters 

#### Success Response

- **`Condition`** : if chapter number is correct.
- **`Response Code`** : `200`
- **`Content example (JSON)`**

``json
{ "error" : "" }
``

#### Error Response

- **`Condition`** : if chapter number conatan wrong value
- **`Response Code`** : `400`
- **`Content example`**

``json
{ "error" : "" }
``

### 8. GET JSON of Slok from Particuler slok & chapter of Shreemad Bhagavad Gita

- **`URL`** : `https://vedicscripturesapi.herokuapp.com/gita{/:ch/:sl}`
- **`Method`** : `GET` 
- **`:ch`** : `[interger]` specfic Adhyay(chapter) number from any of 18 chapters 
- **`Slok num`** : `[interger]` specfic Slok(verse) number avilable in taht particuler `chapter` 

#### Success Response

- **`Condition`** : if chapter and slok num is correct.
- **`Response Code`** : `200`
- **`Content example (SVG)`**

``json
{ "error" : "" }
``

#### Error Response

- **`Condition`** : if chapter num or slok number conatan wrong value
- **`Response Code`** : `400`
- **`Content example`**

``json
{ "error" : "" }
``

#### Source


## 💻 Built with

<img alt="Node.js" src="https://img.shields.io/badge/node.js%20-%2343853D.svg?&style=for-the-badge&logo=node.js&logoColor=white"/>
<img src="https://img.shields.io/badge/express.js%20-%23404d59.svg?&style=for-the-badge"/>
<img src ="https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white"/>
<img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/>

## 🙏 Support ✨
<table>
	<tr>
		<th align="center">
			<a href="https://github.com/ptprashanttripathi">
				<sub><b>Pt. Prashant Tripathi</b></sub>
			</a>
		</th>
  	</tr>
 	<tr>
		<td align="center">
			<a href="https://github.com/ptprashanttripathi">
				<img src="https://avatars2.githubusercontent.com/u/26687933?s=200&v=4" width="100px;" alt=""/>
			</a>
		</td>
	</tr>
</table>  

## Questions and Feedback

**Please contact me using one of the following:**

[![](https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ptprashant09) 
[![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ptprashanttripathi/) 
[![](https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ptprashanttripathi/) 
[![](https://img.shields.io/badge/telegram-%233498DB.svg?&style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ptprashanttripathi/) 
[![](https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/ptprashanttripathi) 
[![](https://img.shields.io/badge/DEV.TO-%230A0A0A.svg?&style=for-the-badge&logo=dev-dot-to&logoColor=white)](https://dev.to/ptprashanttripathi)

<hr>
<p align="center">  
Developed with ❤️ in India 🇮🇳 
</p>
