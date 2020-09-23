"use strict"; //включение "строгого" режима
//Практика

let log = {
	log(msg) {
		console.log(msg);
	}
}

class User {
	static MIN_LENGTH = 3;
	static MIN_LENGTH_PASSWORD = 6;
	
	_login = '';
	_password = '';
	_firstname = '';
	_surname = '';
	_auth = false;
	
	constructor() {
		this.log("Created a new object User");
	}
	
	setLogin(login) {
		if (login.length < User.MIN_LENGTH) throw new Error('Login is too short');
		this._login = login;
	}
	
	setPassword(password) {
		if (password.length < User.MIN_LENGTH_PASSWORD) throw new Error('Password is too short');
		this._password = password;
	}
	
	setFirstname(firstname) {
		if (firstname.length < User.MIN_LENGTH) throw new Error('Firstname is too short');
		this._firstname = firstname;
	}
	
	setSurname(surname) {
		if (surname.length < User.MIN_LENGTH) throw new Error('Surname is too short');
		this._surname = surname;
	}
	
	get name() {
		return this._firstname + ' ' + this._surname
	}
	
	auth() {
		this.log("Connection to database for authorization");
		let result = (this._login == 'admin' && this._password == '123456')
		if (result) {
			this._auth = true;
			this.log("Connection succesfull");
		} else {
			this.log("Auth error");
		}
		return result;
	}
	
	logout() {
		if (this._auth) {
			this._auth = false
			this.log("User leave from system");
		}
	}
	
}

Object.assign(User.prototype, log);

try {
	let user = new User();
	user.setLogin("admin");
	user.setPassword("123456");
	user.setFirstname("Gena");
	user.setSurname("Ivanov");
	console.log(user.name);
	
	user.auth();
	user.logout();
} catch (e) {
	console.log(e);
}