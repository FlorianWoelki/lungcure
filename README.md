# lungcure

## Instructions on testing the webapp

1. Go to https://hidden-peak-62367.herokuapp.com/
2. Login with the email admin@admin.com and password admin
3. Click on the pay with card button and type in the stripe test data (email: admin@admin.com, cardnumber: 4242 4242 4242 4242, date: 01/21 and cvc 545)
4. You're ready to upload your image and let it detect the lung disease for you.


## Configuration

1. Create a copy of `sample.env` with the name `production.env` within the `app` directory.
2. Update `pub_key` and `secret_key` within the `production.env` file with account specific keys.


## Contributors

* [Nishith Choudhary](https://github.com/nishu8?tab=repositories)
* [Sayan Mondal](https://github.com/sayanmondal31)
* [Florian Woelki](https://github.com/FlorianWoelki)
