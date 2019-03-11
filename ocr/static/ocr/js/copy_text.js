function copyText(textElementId, messageElementId) {
  var message = document.getElementById(messageElementId);
  message.className = 'hidden';
  
  /* Get the text field */
  var text = document.getElementById(textElementId);

  /* Select the text field */
  text.select();

  /* Copy the text inside the text field */
  document.execCommand("copy");

  message.className = '';
}