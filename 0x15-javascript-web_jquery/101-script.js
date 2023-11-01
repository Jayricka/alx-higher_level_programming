$(document).ready(function() {
  $('#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function() {
    const listItems = $('ul.my_list li');
    if (listItems.length > 0) {
      listItems.last().remove();
    }
  });

  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
