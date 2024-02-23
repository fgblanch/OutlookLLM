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
    minHeight: "125px",
  },
  
});dfgsdg

const TextInsertion = () => {
  const [text, setText] = useState("Write a cold email to john doe to introduce our marketing services, and propose a brief intro meeting next wednesday. Use the following template [Subject] Subject text... [Body] Message body text...");

  const handleTextInsertion = async () => {
    await insertText(text);sgdfsdfg
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
