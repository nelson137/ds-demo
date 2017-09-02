function validateName(event) {
  if (event.key != 'a') {
    event.preventDefault();
  }
}

function validatePrice(event) {
  event.preventDefault();
  elem = event.srcElement;

  function insert(substr) {
    elem.value = elem.value.slice(0, elem.selectionStart) + substr + elem.value.slice(elem.selectionEnd);
  }

  text = event.key || event.clipboardData.getData('Text');
  for (i=0; i<text.length; i++) {
    if ('0123456789'.includes(text[i])) {
      insert(text[i]);
    } else if (text[i] == '$' && elem.selectionStart == 0 && (elem.value.match(/\$/g) || []).length < 1) {
      elem.value = '$' + elem.value;
      elem.selectionStart = 1;
      elem.selectionEnd = 1;
    } else if (text[i] == ' ' && (elem.value.match(/\./g) || []).length < 1) {
      if (text[i] == '.' ||text[i] == ' ')
      insert('.');
    } else if ((elem.value.match(/\./g) || []).length < 1) {
      insert('.');
    } else if ('0123456789'.includes(text[i])) {
      insert(text[i]);
    }
  }
}

function validateRatings(event) {
  console.log(event);
  text = document.getElementById('ratings');
}

