// only load this piece of code if we're on the donation page
if ($('#donation').length) {

  // set the values for paypal and payment slip
  var changeAmount = function(amount) {
    // update the hidden field used for redirecting to paypal
    $('#id_amount').val(amount);

    // update the amount for generating a payment slip
    $('#id_donation_amount').val(amount);
  };

  var emptyAndReadOnly = function() {
    var checkbox = $(this);
    var donation_amount = $('#id_donation_amount');

    // person would like an empty ESR
    if(checkbox.is(':checked')) {
      donation_amount.val(0);
      donation_amount.attr('readonly', true);
      donation_amount.hide();
      donation_amount.parent().find('span').first().text('–');

    // person would like an ESR with an amount prefilled
    } else {
      donation_amount.attr('readonly', false);
      donation_amount.val($('.md-amount-panel.active').data('amount'));
      donation_amount.show();
      donation_amount.parent().find('span').first().text('CHF');
    }
  };

  var replacePaypalButtonImage = function () {
    $("#md-paypal form input[type='image']")
      .first()
      .attr('src', 'https://www.paypalobjects.com/webstatic/en_US/i/btn/png/gold-rect-paypal-60px.png')
      .height('30')
      .width('97');
  }

  // add a CHF field in front of the donation amount (for ESR)
  $('#id_donation_amount')
    .parent()
    .prepend($('<span />').text('CHF'));

  // change the description text for the option to send a ESR without value in.
  var $checkbox = $('#id_empty_invoice');
  var $checkboxParent = $checkbox.parent();
  $checkboxParent.find('input').first().remove();
  $checkboxParent.prepend($checkbox);
  $checkboxParent.css('text-align', 'left');
  $checkboxParent.find('label').text('Leeren Einzahlungsschein bestellen');

  // fill in the placeholder texts
  $('#id_first_name')
    .attr('placeholder', ($('#trans_id_first_name').val()))
    .prop('required', true);
  $('#id_last_name')
    .attr('placeholder', ($('#trans_id_last_name').val()))
    .prop('required', true);
  $('#id_address')
    .attr('placeholder', ($('#trans_id_address').val()))
    .prop('required', true);
  $('#id_zip')
    .attr('placeholder', ($('#trans_id_zip').val()))
    .prop('required', true);
  $('form textarea')
    .attr('placeholder', ($('#trans_id_comment').val()));

  // set the custom donation value after every change of the input form
  $('#custom-amount').change(function(e) {
    var customAmount = $(this);
    customAmount
      .closest('.md-amount-panel')
      .data('amount', customAmount.val());
    changeAmount(customAmount.val());
  });

  // select a predefined value; and update the paypal & payment slip with the donation value
  $('.md-amount-panel').click(function(e) {
    var amountPanel = $(this);
    changeAmount(amountPanel.data('amount'));
    $('.md-amount-panel.active').removeClass('active');
    amountPanel.addClass('active');
  });

  // set the initial value for paypal and the payment slip
  changeAmount($('.md-amount-panel.active').first().data('amount'));

  // disable the amount value if the donor would like an empty payment slip
  $('#id_empty_invoice').change(emptyAndReadOnly);

  // extract and set the redirect_url where the donor will be redirected to after donating money
  $('#id_invoice_redirect_url').val($('#invoice_redirect_url').val());

  var sizeDonationPanels = function () {
    // get all the panels
    var $panels = $('#donation div.md-amount-panel .panel');

    // reset the hard-set height, so we can get the actual height the element needs
    $panels.css('height', '');

    // figure out the height of the highest panel
    var highestPanelHeight = 0;
    $panels.each(function() {
      var panelHeight = $(this).height();
      if (panelHeight > highestPanelHeight) {
        highestPanelHeight = panelHeight;
      }
    });

    // set the height of all the panels to the same height as the highest panel
    $panels.css('height', highestPanelHeight);
  }

  $(window).resize(sizeDonationPanels);
  sizeDonationPanels();
  replacePaypalButtonImage();
}

