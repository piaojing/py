function myFunction() {
  var del_conf = window.confirm();
  if (del_conf == true) {
    return (window.theForm.action = "process_delete.py");
  } else {
    return false;
  }
}
