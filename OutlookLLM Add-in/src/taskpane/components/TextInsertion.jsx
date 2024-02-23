import * as React from "react";
import { useState } from "react";
import { Button, Field, Title3, Textarea, tokens, makeStyles } from "@fluentui/react-components";
import insertText from "../office-document";

const useStyles = makeStyles({
  
  textPromptAndInsertion: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  textAreaField: {
    marginLeft: "15px",
    marginTop: "30px",
    marginBottom: "15px",
    marginRight: "15px",
    minHeight: "150px",
  },
  
});

const TextInsertion = () => {
  const [text, setText] = useState("Write a cold email to john doe to introduce our marketing services, and propose a brief intro meeting next wednesday.");



  const handleTextInsertion = async () => {
    try {
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
      
      const textContent = await response.text();
      await insertText(textContent);

    } catch (error) {
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
      <Field className={styles.textAreaField} size="medium" label="Describe the email you need AI help you with:">
        <Textarea size="medium" className="{styles.textArea}" placeholder={text} onChange={handleTextChange} resize="vertical"/>
      </Field>
      <Button appearance="primary" disabled={false} size="large" onClick={handleTextInsertion}>
        Compose draft with AI.
      </Button>
    </div>
  );
};

export default TextInsertion;
