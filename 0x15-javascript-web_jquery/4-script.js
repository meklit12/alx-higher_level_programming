const $headerElem = $('header');
const $divRedHeader = $('DIV#toggle_header');

$divRedHeader.on('click', () => {
  const currentClass = $headerElem.attr('class');
