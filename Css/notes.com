Css- Cascading style sheet
-It is used to give on html elements.
-It is used to create layout of web application/ website


Types of Css
1) inline css- it is applied on html elements.
        for eg-<p style={color:red}> the Kathmandu</p>

2) Internal css- it is applied or used on same html file, inbetween head

        for eg- 
         <style>
                    property:Value
                    selector->p{
                    color: blue;
                    font-size: 2 rem;
        }
    </style>

3) External Css- It is  used by add link of external css file on html file


Margin-border dheki contain samma ko gap lai Margin
margin-left: 5px;
margin-right: 5px;
margin-top: 5px;
margin-bottom: 5px;


margin: 5px(top) 5px(right) 5px(bottom) 5px(left);

margin: 5px(top ra bootom lai dincga aarko dui ta value le right ra left ko value dincha) 6px 7px 

margin : 5px 7px

position:
 1. Static Position:
 2. Relative Position:
 3. Abslute Position:
 4. Sticky Position:
 5. Fixed Position:
