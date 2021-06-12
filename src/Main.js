import React, { Component } from "react";
import Radio from '@material-ui/core/Radio';
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import RadioGroup from '@material-ui/core/RadioGroup';




 
class Main extends Component {
	


constructor(props) {
  super(props);
   this.state = {
     selectedOption: "option1"
  };
  
  
  
}


handleOptionChange = changeEvent => {
    this.setState({
      selectedOption: changeEvent.target.value
    });
  };
  

render() {
	
	
 return(
 
 
	
 
  <div id="parent">
    <div id="questions" style={{
      margin: 'left',
      display: 'inline-block',
      width: '60%'
    }}>
      <h3>Lets help you select a wine for your taste buds:</h3>

      <FormControl component="fieldset">

      <FormLabel component="legend">1. Style: Red Wine, White Wine, or Enjoys both style.</FormLabel>
      <RadioGroup aria-label="style" name="style"	onChange={this.handleOptionChange}  >
        <FormControlLabel value="red" control={<Radio />} label="Red (only)" />
        <FormControlLabel value="white" control={<Radio />} label="White (only)" />
        <FormControlLabel value="both" control={<Radio />} label="Both (enjoys both styles)" />
      </RadioGroup>

      <FormLabel component="legend">2. Body: how heavy or dense the wine feels when tasting. (thin watery taste would be “Low”….more Hearty heavy taste would be “Full” : </FormLabel>
      <RadioGroup aria-label="body" name="body" >
        <FormControlLabel value="light" control={<Radio />} label="Light" />
        <FormControlLabel value="medium" control={<Radio />} label="Medium" />
        <FormControlLabel value="full" control={<Radio />} label="Full" />
      </RadioGroup>


<FormLabel component="legend">3. Alcohol: the sharpness of the taste that ranges in an area of soft n mellow= light, a more striking taste that resembles a shot of liquor= Very High </FormLabel>
      <RadioGroup aria-label="alcohol" name="alcohol" >
        <FormControlLabel value="light" control={<Radio />} label="Light" />
        <FormControlLabel value="medium" control={<Radio />} label="Medium" />
        <FormControlLabel value="high" control={<Radio />} label="High" />
      </RadioGroup>



<FormLabel component="legend">4. If you are by the numbers this is the range to refer to…</FormLabel>
      <RadioGroup aria-label="range" name="range" >
        <FormControlLabel value="ultralow" control={<Radio />} label="12-15%" />
        <FormControlLabel value="low" control={<Radio />} label="12-12.5%" />
        <FormControlLabel value="medium" control={<Radio />} label="13.5-14.5%" />
<FormControlLabel value="high" control={<Radio />} label="14.5-15.5%" />
<FormControlLabel value="veryhigh" control={<Radio />} label="15-17%" />
      </RadioGroup>

<FormLabel component="legend">5. Acidity: the feel on Mid-Palette (before you swallow) that resembles a “pin & needles” feel on your tongue. (Think of how carbonation effects your palette when drinking a carbonated beverage)</FormLabel>
      <RadioGroup aria-label="acidity" name="acidity" >
          <FormControlLabel value="low" control={<Radio />} label="Low" />
        <FormControlLabel value="medium" control={<Radio />} label="Medium" />
        <FormControlLabel value="high" control={<Radio />} label="High" />
      </RadioGroup>


<FormLabel component="legend">6. Tannins: on the Front Palette (the first taste) and Mid Palette that makes you pucker…think of a reaction of something sour but in a good way. 
</FormLabel>
      <RadioGroup aria-label="tannins" name="tannins" >
          <FormControlLabel value="low" control={<Radio />} label="Low" />
        <FormControlLabel value="medium" control={<Radio />} label="Medium" />
        <FormControlLabel value="high" control={<Radio />} label="High" />
      </RadioGroup>


   </FormControl>
    </div>
  <div id="images" style={{
      margin: 'auto',
      display: 'block',
      width: '50%'
    }}>
   
  </div>
</div>
  );
}
 }

export default Main;