'use strict'

/**
 * Fix num cores
 */
function fix_num_cores() {
  let node_type_input = $('#batch_connect_session_context_node_type');
  let max = (node_type_input.val() === ':hugemem') ? 48 : 28;
  let num_cores_input = $('#num_cores');
  let num_cores_value = num_cores_input.val();

  num_cores_input.attr('max', max);
  num_cores_input.val(Math.min(max, num_cores_value));
}


/**
 * Change the maximum number of cores selected.
 */
function set_node_type_change_handler() {
  let node_type_input = $('#batch_connect_session_context_node_type');
  node_type_input.change(node_type_input, fix_num_cores);
}

$(document).ready(function() {
  // Set the max value to be what was set in the last session
  fix_num_cores();
  set_node_type_change_handler();
});