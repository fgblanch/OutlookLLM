/* global Office console */

const insertText = async (text, writeSubject) => {
  // Write text to the cursor point in the compose surface.
  try {
    if (writeSubject) {
      const respSetSubject = await Office.context.mailbox.item.subject.setAsync(
        text.subject,
        { coercionType: Office.CoercionType.Text },
        (asyncResult) => {
          if (asyncResult.status === Office.AsyncResultStatus.Failed) {
            throw asyncResult.error.message;
          }
        }
      );  
    }

    const respSetBody = await Office.context.mailbox.item.body.setSelectedDataAsync(
      text.body,
      { coercionType: Office.CoercionType.Text },
      (asyncResult) => {
        if (asyncResult.status === Office.AsyncResultStatus.Failed) {
          throw asyncResult.error.message;
        }
      }
    );

  } catch (error) {
    console.log("Error: " + error);
  }
};

export default insertText;
