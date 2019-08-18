/* Jest Test Cases */
import React from 'react';
import {shallow} from 'enzyme';
import ExampleWorkModal from '../js/example-work-modal'

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import { exportAllDeclaration } from '@babel/types';

Enzyme.configure({adapter: new Adapter()});

const myExample = {
		'title' : "Serverless Portfolio",
		'href' : "https://example.com",
		'desc' : "My Serverless Portoflio with CICD",
		'image' : {
			'desc': "example screenshot of a project involving code",
			'src' : "images/portfolio_example1.png",
			'comment' : `First Project`
	}
};


describe("ExampleWorkModal component", () => {
	let component = shallow(<ExampleWorkModal example={myExample} open={false}/>);
	let openComponent = shallow(<ExampleWorkModal example={myExample} open={true}/>);
	let anchors = component.find("a");

	it("Should contain a single 'a' element", () => {
		expect(anchors.length).toEqual(1);
	});

	it("Should link to our project", () => {
		expect(anchors.prop('href')).toEqual(myExample.href);
	});

	it("Should have the model class set correctly", () => {
		expect(component.find(".background--skyBlue").hasClass('modal--closed')).toBe(true);
		expect(openComponent.find(".background--skyBlue").hasClass('modal--open')).toBe(true);
	});
});