const React = require('react');
const ReactDOM = require('react-dom/client');
const e = React.createElement;

var imageStyle = {
  margin: '10px',
  display: 'inline-block'
};

class ImageBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentImage: this.props.imageStart
    };
  }
  
  click(image) {
    this.setState({
      currentImage: image
    });
  }
  
  render() {
    const images = this.props.images.map((i) =>
      e(
        'div', {style: imageStyle, className: 'image', key: i.image},
        e('img',
          {
            onClick: this.click.bind(this, i),
            width: '100',
            src: i.thumbnail
          }
        ) // end element 'img'
      ) // end element 'div'
    );
    return e('div', {className: 'gallery'},
             e('div', {className: 'current-image'},
               e('img', {src: this.state.currentImage.image})
             ),
             images,
           ); // end element className 'gallery'
  } // end render
} // end class ImageBox

window.React = React;
window.ReactDOM = ReactDOM;
window.ImageBox = ImageBox;

module.exports = ImageBox;

