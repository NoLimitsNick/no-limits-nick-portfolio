import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work'


const myWork = [
	{
		'title' : "Serverless Portfolio",
		'href' : "https://github.com/NoLimitsNick/no-limits-nick-portfolio",
		'desc' : "My Serverless Portoflio Built using DevOps Practices",
		'image' : {
			'desc': "",
			'src' : "images/portfolio_example1.png",
			'comment' : `First Project`
		}
	},
	{
		'title' : "Senior Design RFID Inventory Microservices",
		'href' : "https://github.com/NoLimitsNick/M6E-RFID-Inventory",
		'desc' : "Senior Design Microservice Architecture",
		'image' : {
			'desc': "Senior Design Project Architecture",
			'src' : "images/seniordesign_example2.png",
			'comment' : `Second Project`
		}
	},
	{
		'title' : "Pi Embedded SQLite Express API ",
		'href' : "https://github.com/NoLimitsNick/Pi-Embedded-Sqlite-API",
		'desc' : "IoT + Network Security + SQL",
		'image' : {
			'desc' : "Express API written for Embedded PI SQLite",
			'src' : "images/sqlwebform_example3.png",
			'comment' : `Third Project`
		}
	}
]
ReactDOM.render(<ExampleWork work = {myWork}/>, document.getElementById('example-work'));