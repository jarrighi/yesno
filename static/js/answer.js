var answerButtons = document.querySelectorAll(".answer .button");
for (var i = 0; i < answerButtons.length; i++) {
    answerButtons[i].addEventListener('click', function() {
        var choice = this.dataset.choice;
        var endpoint = '/answer/' + qid + "/" + choice;
        $.ajax({
            url: endpoint,
            error: function() {
                console.log("Ajax request failed.");
            },
            success: function(data) {
                var percentYes = Math.round((data.yesses / ( data.yesses + data.nos)) * 100);
                var percentNo = (100 - percentYes);

                var data_html = '<div class="record"><div class="bar" style="width:' + percentYes
                + '%;"><span>Yes</span></div><div class="p"><span>' + data.yesses
                + '</span></div></div><div class="record"><div class="bar" style="width:'
                + percentNo + '%;"><span>No</span></div><div class="p"><span>'
                + data.nos + '</span></div></div>';

                $('#data').html(data_html);
            }
        });
    });
};
