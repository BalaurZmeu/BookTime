const React = require('react');
const ImageBox = require('./imageswitcher');
const renderer = require('react-test-renderer');
const Enzyme = require('enzyme');
const Adapter = require('@cfaester/enzyme-adapter-react-18');

Enzyme.configure({ adapter: new Adapter() });

test
