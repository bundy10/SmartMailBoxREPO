import React, { Component, useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Button from './Button';
import { config } from '../config.js'


class Panel extends Component {

  constructor(props){

    super(props);

    this.handleClick = this.handleClick.bind(this);
    this.handleSwitchStatus = this.handleSwitchStatus.bind(this);
    this.state = {switchStatus: 1}

  }


  sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }

  notify = () => {
    toast.info( '🚚 Delivery Arrived!!! Please Accept Delivery!',
    {
    position: "bottom-right",
    autoClose: 500000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: "light",
    });
};


  async notification() {
    {
      this.state.switchStatus == 0 ?
      this.notify(): 
      <p>BUTTON NOT PRESSED</p>
    }
  }
  

  handleClick(action) {

    var formData  = new FormData();

    formData.append('action', action);

    fetch(config.backend_url, {
      mode: 'no-cors',
      method: 'POST',
      body: formData
    }).then(function(response) {  
      
    });

  }

  handleSwitchStatus() {
    
    fetch(config.backend_url + '/switch')
    .then( res => {
        if (res.status == 200) {
          // console.log(res)
          res.json().then(data => {
            this.setState({switchStatus: data})
            console.log(data)
        })
      }
    })
  }
  



  render() {

    var style = {
      'width': '100%',
      'display': 'flex',
      'height': '100px',
      'justify-content': 'center',
      'zIndex': '20'
    };
    
    var styleD = {
      'display': 'flex',
      'height': '150px',
      'zIndex': '20',
      'bottom:': '1000px',
      'right:': '500px',
      'position': 'bottom-right'
    };


    var buttons;

    buttons = this.props.buttons.map(button => {

      return (<Button label={button.name} key={button.id} action={button.action} onClick={this.handleClick.bind(this)} />)

    });


    this.handleSwitchStatus()
    this.notification()

    return (
      <div classname='Panel' style={style}>
        { buttons[0] }
        { buttons[1] }
        { buttons[2] }
        {/* {this.handleSwitchStatus()} */}
        {/* <p>Switch Status: {this.handleSwitchStatus()}</p> */}
        <ToastContainer />
        { /* <button onClick={this.notify}>Notify!</button> */}
        
      </div>
      
    );
  }

}

export default Panel;
