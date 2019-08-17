import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work'

const myWork = [
	{
		'title' : "Serverless Portfolio",
		'image' : {
			'desc': "example screenshot of a project involving code",
			'src' : "images/portfolio_example1.png",
			'comment' : `First Project`
		}
	},
	{
		'title' : "Senior Design RFID Inventory Microservices",
		'image' : {
			'desc': "Senior Design Project Architecture",
			'src' : "images/seniordesign_example2.png",
			'comment' : `Second Project`
		}
	},
	{
		'title' : "Pi Embedded SQLite Express API ",
		'image' : {
			'desc' : "Express API written for Embedded PI SQLite",
			'src' : "images/sqlwebform_example3.png",
			'comment' : `Third Project`
		}
	}
]
ReactDOM.render(<ExampleWork work = {myWork}/>, document.getElementById('example-work'));