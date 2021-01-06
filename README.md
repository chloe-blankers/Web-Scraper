# Web-Scraper
This Python program reads HTML tables and converts them into csv format.

### Example Input Table
<table>
    <tr>
        <th>Student Number</th>
        <th>Student Name</th>
        <th>Major</th>
        <th>A1 mark</th>
        <th>A2 mark</th>
    </tr  >
    <tr> 
        <td>V00000001</td>
        <td>Will Byers</td>
        <td>Paranormal Studies</td> 
    </tr>
    <tr>
        <td>V00123456</td>
        <td>Alastair      Avocado</td>
        <td>   Psychology</td>
        <td>12</td>
        <td></td>
    </tr>
    <tr>
        <td>V00123457</td>
        <td>Rebecca Raspberry</td>
        <td>Computer Science</td>
        <td>17</td>
        <td>14</td>
    </tr>
    <tr>
        <td>V00314159</td>
        <td>Fiona Framboise</td>
        <td style="font-family: monospace; font-size: 20pt;"> Computer Science</td>
        <td>         </td>
        <td>17</td>
    </tr>
    <tr>
        <td>V00654321</td>
        <td>Meredith Malina</td>
        <td style="color: red;">Software Engineering</td>
        <td>18</td>
        <td>12</td>
    </tr>
    <tr>
        <td>V00654322</td>
        <td>Hannah Hindbaer</td>
        <td>Physics</td>
        <td>15</td>
        <td>18</td>
    </tr>
    <tr>
        <td></td>
        <td>Neal Naranja</td>
        <td>Anthropology</td>
        <td>15</td>
        <td>15</td>
    </tr>
</table>
<br />

<table>
    <tr>
        <th>Movie Title</th>
        <th>ID</th>
        <th>Genre</th>
        <th>Rating</th>
        <th>Director</th>
        <th>Year</th>
    </tr  >
    <tr> 
        <td>Thor: Ragnarok</td>
        <td>0001</td>
        <td>Action</td>
        <td>8.2</td> 
        <td>Taika Waititi</td>
        <td>2017</td>
    </tr>
    <tr> 
        <td>Star Wars: The Last Jedi</td>
        <td>00111</td>
        <td>Sci-Fi</td>
        <td></td> 
        <td>Rian Johnson</td>
        <td>2017</td>
    </tr>
    <tr> 
        <td>Fight Club</td>
        <td>0201</td>
        <td>Drama</td>
        <td>8.8</td> 
        <td class="dir">David Fincher</td>
        <td>1999</td>
    </tr>
    <tr> 
        <td> Amélie</td>
        <td>1221</td>
        <td>Comedy</td>
        <td>8.2</td> 
        <td class="dir" style="font-size : 20px;"  >Jean-Pierre Jeunet</td   >
        <td>2001</td>
    </tr>
</table>
<br />

<table>
    <tr>
        <th>Album Name</th>
        <th>Artist</th>
        <th>Genre</th>
        <th>Rating</th>
    </tr  >
    <tr> 
        <td>Singing Saw</td>
        <td> Kevin Morby</td>
        <td>Indie Rock</td> 
        <td>8.1</td>
    </tr>
    <tr> 
        <td>Kid A</td>
        <td> Radiohead</td>
        <td>Alternative Rock</td> 
        <td>9.5</td>
    </tr>
    <tr> 
        <td>Transformer</td>
        <td> Lou Reed</td>
        <td> Glam Rock</td> 
        <td>9.9</td>
    </tr>
    <tr>
        <td>Aladdin Sane</td>
        <td><strong>David Bowie</strong></td>
        <td>Art Rock</td> 
        <td>8.7</td>
    </tr>
    <tr>
        <td>Wish You Were Here</td>
        <td> Pink Floyd</td>
        <td>Prog Rock</td> 
        <td>9.5</td>
    </tr>
    <tr>
        <td>Missing Data Row</td>
        <td></td>
    </tr>
</table>
<br />


### Example Output CSV File
TABLE 1:</br>
Student Number,Student Name,Major,A1 mark,A2 mark</br>
V00000001,Will Byers,Paranormal Studies,,</br>
V00123456,Alastair Avocado,Psychology,12,</br>
V00123457,Rebecca Raspberry,Computer Science,17,14</br>
V00314159,Fiona Framboise,Computer Science,,17</br>
V00654321,Meredith Malina,Software Engineering,18,12</br>
V00654322,Hannah Hindbaer,Physics,15,18</br>
,Neal Naranja,Anthropology,15,15</br>
</br>
TABLE 2:</br>
Movie Title,ID,Genre,Rating,Director,Year</br>
Thor: Ragnarok,0001,Action,8.2,Taika Waititi,2017</br>
Star Wars: The Last Jedi,00111,Sci-Fi,,Rian Johnson,2017</br>
Fight Club,0201,Drama,8.8,David Fincher,1999</br>
Amélie,1221,Comedy,8.2,Jean-Pierre Jeunet,2001</br>
</br>
TABLE 3:</br>
Album Name,Artist,Genre,Rating</br>
Singing Saw,Kevin Morby,Indie Rock,8.1</br>
Kid A,Radiohead,Alternative Rock,9.5</br>
Transformer,Lou Reed,Glam Rock,9.9</br>
Aladdin Sane,<strong>David Bowie</strong>,Art Rock,8.7</br>
Wish You Were Here,Pink Floyd,Prog Rock,9.5</br>
Missing Data Row,,,</br>





