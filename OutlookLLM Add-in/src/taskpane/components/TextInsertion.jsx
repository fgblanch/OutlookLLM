import * as React from "react";
import { useState } from "react";
import { Button, Field, Title3, Checkbox, Textarea, Text, Spinner, tokens, makeStyles } from "@fluentui/react-components";
import insertText from "../office-document";

const useStyles = makeStyles({
  
  textPromptAndInsertion: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "flex-start"
  },

  textField: {
    marginLeft: "15px",
    marginTop: "30px",
    marginRight: "15px",
    
  },

  textAreaField: {
    marginLeft: "15px",
    marginTop: "10px",
    
    marginRight: "15px",
    minHeight: "150px",
  },

  textCheck: {
    marginTop: "10px",
    marginLeft: "15px",
    marginRight: "15px",
    
  },

  checkStyle: {
    marginBottom: "15px",
  }
  
});

const TextInsertion = () => {
  const [text, setText] = useState("Write a cold email to introduce our marketing services, and propose a brief intro meeting next wednesday.");
  const [showSpinner, setshowSpinner] = useState(false);
  const [writeSubject, setWriteSubject] = useState(false);


  const handleTextInsertion = async () => {
    try {
      
      setshowSpinner(true);
      
      const response = await fetch("https://localhost:8385/composeEmail", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          prompt: text,
        })
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      // Handle success response if needed
      console.log('Data sent successfully');
    
      const textContent = await response.json();
      await insertText(textContent, writeSubject);
      setshowSpinner(false);

    } catch (error) {
      setshowSpinner(false);
      console.error('Error sending data:', error);
    }

    
  };

  const handleTextChange = async (event) => {
    setText(event.target.value);
  };

  const styles = useStyles();

  return (
    <div className={styles.textPromptAndInsertion}>
      <Title3>Compose with AI</Title3>
      <Text className={styles.textField} size="medium" >1. Set the cursor where you want to insert the AI generated email.</Text>
      <Field className={styles.textAreaField} size="medium" label="2. Describe the email you need AI help you with:">
        <Textarea size="medium" className="{styles.textArea}" placeholder={text} onChange={handleTextChange} resize="vertical"/>
      </Field>
      <Text className={styles.textCheck} size="medium" >3. Check if you want also AI to generate the email subject.</Text>
      <Checkbox className={styles.checkStyle}  label="Generate Email Subject" onChange={(ev, data) => setWriteSubject(data.checked)} value={writeSubject}/>
      <Button appearance="primary" disabled={false} size="large" onClick={handleTextInsertion}>
        {showSpinner && (
          <Spinner  id="spinner" appearance="inverted"/>
        )} 
        {showSpinner ? '   Generating email...' : 'Compose with AI'}
      </Button>
      
    </div>
  );
};

export default TextInsertion;
