var invalidPrice = false;
var invalidRatings = false;

function validatePrice(event) {
  text = event.srcElement.value;
  invalid = false;
  for (i=0; i<text.length; i++) {
    if (! '0123456789.'.includes(text[i])) {
      invalid = true;
    }
  }
  if ((text.match(/\./g) || []).length > 1) {
      invalid = true;
  }

  icon = document.getElementById('warn-icon-price');
  if (invalid) {
    icon.style.display = 'block';
    invalidPrice = true;
  } else {
    icon.style.display = 'none';
    invalidPrice = false;
  }
}

function validateRatings(event) {
  text = event.srcElement.value;
  invalid = false;
  for (i=0; i<text.length; i++) {
    if (! '0123456789'.includes(text[i])) {
      invalid = true;
    }
  }

  icon = document.getElementById('warn-icon-ratings');
  if (invalid) {
    icon.style.display = 'block';
    invalidRatings = true;
  } else {
    icon.style.display = 'none';
    invalidRatings = false;
  }
}

function onSubmit() {
  if (! invalidPrice && ! invalidRatings) {
    return true;
  } else {
    if (invalidPrice) { console.log('Price field is invalid'); }
    if (invalidRatings) { console.log('Ratings field is invalid'); }
    return false;
  }
}

