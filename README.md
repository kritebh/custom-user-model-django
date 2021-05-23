## Custom User Model In Django

Django provides a User model in which you can create account and do basic stuff.

But this is not enough for custom web-apps

- Login from email instead of username
- Add own custom field such as Date Of Birth,City etc.

However if you want to just extend the User model with some another fields then you can use OneToOne relationship.

> [Extend User Model](https://github.com/kritebh/extend-user-model-django)
