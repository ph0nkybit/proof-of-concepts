## Overview

ALF-BanCo is a homebanking software that manages accounts in various banks, Paypal accounts and many credit cards. The software saves transactions on the PC for as long as the user requires.

## Discovered By

**[Nicolò Tescari](https://www.linkedin.com/in/nicol%C3%B2-tescari-913390131/) ([@ph0nkybit](https://twitter.com/ph0nkybit))** of **[Cybertech](https://www.cybertech.eu/)**

## Proof of Concept (PoC)

The application uses a hardcoded default password to encrypt the local SQLite database containing the user's data. An attacker who gains physical or remote access to the user's machine can exploit this vulnerability to read and modify the data.

The vulnerability was discovered on **ALF-BanCO 8.2.3 (Profi version)**. According to the vendor, it is present up to version **8.2.5**. A patch has been released starting with version **8.3.0**.

At the request of the vendor, the password has been partially obscured.

* * *

After installing the application and configuring our user, the file “**HbDat001.alfdb8**” is created inside the following path: “**C:\\Users\\&lt;username&gt;\\AppData\\Roaming\\ALFBanCo8\\Daten**”.
