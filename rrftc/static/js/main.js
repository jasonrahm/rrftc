/**
 * Created by rahm on 2/14/16.
 */

jQuery(document).ready(function() {
    $("input#a_climbers").change(function () {
        if (this.checked) {
            $('div#a_climbers_acc.form-group').show();
        } else {
            $('div#a_climbers_acc.form-group').hide();
        }
    });
    $("input#a_midpark").change(function () {
        if (this.checked) {
            $('div#a_midpark_acc.form-group').show();
        } else {
            $('div#a_midpark_acc.form-group').hide();
        }
    });
    $("input#a_highpark").change(function () {
        if (this.checked) {
            $('div#a_highpark_acc.form-group').show();
        } else {
            $('div#a_highpark_acc.form-group').hide();
        }
    });
    $("input#t_climbers").change(function () {
        if (this.checked) {
            $('div#t_climbers_acc.form-group').show();
        } else {
            $('div#t_climbers_acc.form-group').hide();
        }
    });
    $("input#lowclimber").change(function () {
        if (this.checked) {
            $('div#lowclimber_acc.form-group').show();
        } else {
            $('div#lowclimber_acc.form-group').hide();
        }
    });
    $("input#midclimber").change(function () {
        if (this.checked) {
            $('div#midclimber_acc.form-group').show();
        } else {
            $('div#midclimber_acc.form-group').hide();
        }
    });
    $("input#highclimber").change(function () {
        if (this.checked) {
            $('div#highclimber_acc.form-group').show();
        } else {
            $('div#highclimber_acc.form-group').hide();
        }
    });
    $("input#t_midpark").change(function () {
        if (this.checked) {
            $('div#t_midpark_acc.form-group').show();
        } else {
            $('div#t_midpark_acc.form-group').hide();
        }
    });
    $("input#t_highpark").change(function () {
        if (this.checked) {
            $('div#t_highpark_acc.form-group').show();
        } else {
            $('div#t_highpark_acc.form-group').hide();
        }
    });
});
