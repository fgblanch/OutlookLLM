/* global Office console */

const insertText = async (text) => {
  // Write text to the cursor point in the compose surface.
  try {
    Office.context.mailbox.item.body.setSelectedDataAsync(
      text,
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
