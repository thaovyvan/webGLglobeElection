$(document).ready(function()
{
    var colors = [0x0066ff, 0xe20800, 0];
    var globe = DAT.Globe($('#container')[0], function(label)
    {
      return new THREE.Color(colors[label]);
    });

    $('.tweet').show();

    $('.tweet').each(function(i)
    {
      var htmlcolor = colors[i].toString(16);
      htmlcolor = '000000'.substr(0, 6 - htmlcolor.length) + htmlcolor;
      $(this).css('border-left', '20px solid #'+htmlcolor);
      if (i < 2)
      {
        $(this).click(function()
        {
          displayData(i+1);
          $('.tweet').removeClass('active');
          $(this).addClass('active');
        });
      }
    });

    $('#sAll').click(function()
    {
      displayData(false);
      $('.tweet').removeClass('active');
    })

    function displayData(label)
    {
      globe.resetData();
      globe.addData(window.data, {format: 'legend', showLabel: label});
      globe.createPoints();
    }

    $.ajax({
      url: 'data.json',
      dataType: 'json',
      data: {},
      cache: false,
      success: function(data)
      {
        window.data = data;
        displayData(false);
        globe.animate();
        $('#sAll').html('Show all tweets');
      },
      error: function(jqXHR, textStatus, errorThrown)
      {
        alert('Error downloading data: '+textStatus);
      }
    });
});
