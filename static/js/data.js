$(document).ready(function () {
    $('#show-data').click(function() {
        var endpoint = '/answers/' + qid;
        $.ajax({
            url: endpoint,
            error: function() {
                $('#info').html('oops');
            },
            success: function(data) {
                var data_html = "<p>People who answered yes: " + data.yesses
                    + "</p> <p>People who answered no: " + data.nos + "</p>";
                $('#data').html(data_html);
            }
        });
    });
});