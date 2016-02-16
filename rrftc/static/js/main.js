/**
 * Created by rahm on 2/14/16.
 */

jQuery(document).ready(function() {
    $("input#auto.form-control").change(function () {
        if (this.checked) {
            $('div#beacon.form-group').show();
        } else {
            $('div#beacon.form-group').hide();
        }
    });
});
