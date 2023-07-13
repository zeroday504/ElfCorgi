# UndercoverCorgi
CLI for Elf Qrin's sock puppet account generator

## What is a sock puppet account?
A sock puppet account is a fake persona used for online interactions. These can be used during OSINT investigations or when a user is trying to prevent successful attribution to their online activity. There's an excellent write-up on sock puppet accounts here: 
https://ztrkouzhan.medium.com/the-mega-sock-puppets-tutorial-for-osint-af3bd29dd5fc

## What is Elf Qrin's sock puppet account generator?
Elf Qrin is a web page that generate's beefy profiles for fake personas. The web page can be found here: https://elfqrin.com/fakeid.php

## What does UndercoverCorgi do?
This tool interacts with Elf Qrin's web page to generate fake personas and outputs the data into a parsable, greppable file. All the details will be saved into a txt file on your endpoint as well as output to the screen.

## Usage
`python3 UndercoverCorgi.py`

## Example Output

```
_  _ _  _ ___  ____ ____ ____ ____ _  _ ____ ____    ____ ____ ____ ____ _
|  | |\ | |  \ |___ |__/ |    |  | |  | |___ |__/    |    |  | |__/ | __ |
|__| | \| |__/ |___ |  \ |___ |__|  \/  |___ |  \    |___ |__| |  \ |__] |
--------------------------------------------------------------------------
            CLI for Elf Qrin's sock puppet account generator


Select gender of sock puppet account (m or f): f

Establishing connection to Elf Qrin's Lab...

Successful connection, generating sock puppet account...

Gender: Female

First name: Juanita

Middle name: Jacqueline

Last name: Harrison

Initials: J. J. H.

Mother's Maiden name: Ramos

Birthday: February, 17 1985 (Age: 38 years)

Birthplace: San Rafael, CA, USA 

Zodiacal sign: Aquarius

User name: harrisjua

Password: 8bw666nu 

Password hash (MD5): ce4b9cff5433a538ffd9faf2f807f682

Password hash (SHA1): 7ee974f68fccdd322b505d8ab4737c96390d820e

E-Mail: harrisjua@safetymail.info (It's a real address: check it)

Phone: 757-382-6637

Address: 44 Stevenson Rd, Stevenson, MD 21153, USA 

SSN: 553571153 - issued in California (CA)

PassportNo.: : 555270797issued: October/22/2020expires: October/21/2030P<USAHARRISON<<JUANITA<JACQUELINE<<<<<<<<<<<5552707973USA8502175F3010219<<<<<<<<<<<<<<06

Driver License: H-625-331-884-420 - issued in Maryland (MD) on 03/10/2022, expires 02/17/2028

Car: Chevrolet Equinox

Car License Plate: 6YUX879 - issued in California (CA) in year 2015

Hair color: Black (BLK)

Eyes color: Hazel (HZL)

Height: 170 cm / 5 ft 7 in

Weight: 57 Kg / 126 pounds

Shoe Size: 8

Blood Type: A+ (Can donate to: A+, AB+ ; Can receive from: 0-, 0+, A-, A+ )

Religion: Protestant

Political side: Republican

Favorite Color: Blue

Favorite Comfort Food: Chocolate

Favorite Cereal: Rice Krispies

Favorite Season: Fall

Favorite Animal: Elephant

Lucky Number: 4

Preparer Tax Identification Number (PTIN): P88045642

Interim PTIN (temporary PTIN): P99991153

Employer Identification Number (EIN): 506081477

Individual Taxpayer Identification Number (ITIN): 943782551

Adoption Taxpayer Identification Number (ATIN): 790245451


Output has been saved in the current directory as sockpuppetfile.txt
```
