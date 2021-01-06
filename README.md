# Web-Scraper
This Python program reads HTML tables and converts them into csv format.

### Example Input Table
<table><tr>
<th>Student Number</th><th>Student Name</th><th>Major</th>
<th>A1 mark</th><th>A2 mark</th></tr  >
<tr><td>V00000001</td><td></td><td></td><td>10</td>
<td>11</td>
</tr>
<tr><td>V00123456</td><td>Alastair Avocado</td>
<td>Psychology</td><td>12</td><td></td></tr>
<tr  >
<td>V00123457</td >
<td>Rebecca Raspberry
</td><td>Computer Science</td><td>17</td><td>14</td></tr>
<tr><td>V00314159</td><td>Fiona Framboise</td>
<td style="font-family: monospace; font-size: 20pt; font-weight: bold;">
Computer Science
</td>
<td>   </td><td>17</td></tr>
<tr><td>V00654321</td><td>Meredith Malina</td>
   <td style="color: red;">Software Engineering</td><td>18</td><td>12</td></tr>
<tr><td>V00654322</td><td>Hannah Hindbaer</td><td>Physics</td><td>15</td><td>18</td></tr>
<tr><td>V00951413</td><td>Neal Naranja</td><td>Anthropology</td><td>15</td><td>15</td></tr>
</table>

### Example Output CSV File
Student Number,Student Name,Major,A1 mark,A2 mark</br>
V00000001,,,10,11</br>
V00123456,Alastair Avocado,Psychology,12,</br>
V00123457,Rebecca Raspberry,Computer Science,17,14</br>
V00314159,Fiona Framboise,Computer Science,,17</br>
V00654321,Meredith Malina,Software Engineering,18,12</br>
V00654322,Hannah Hindbaer,Physics,15,18</br>
V00951413,Neal Naranja,Anthropology,15,15</br>




