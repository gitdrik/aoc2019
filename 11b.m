P = [3,8,1005,8,290,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,28,1006,0,59,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,53,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,76,1006,0,81,1,1005,2,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,105,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,126,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,148,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,171,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,193,1,1008,8,10,1,106,3,10,1006,0,18,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,225,1,1009,9,10,1006,0,92,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,254,2,1001,8,10,1,106,11,10,2,102,13,10,1006,0,78,101,1,9,9,1007,9,987,10,1005,10,15,99,109,612,104,0,104,1,21102,1,825594852136,1,21101,0,307,0,1106,0,411,21101,0,825326580628,1,21101,0,318,0,1105,1,411,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179557207043,1,1,21101,0,365,0,1106,0,411,21101,0,46213012483,1,21102,376,1,0,1106,0,411,3,10,104,0,104,0,3,10,104,0,104,0,21101,988648727316,0,1,21102,399,1,0,1105,1,411,21102,988224959252,1,1,21101,0,410,0,1106,0,411,99,109,2,21201,-1,0,1,21101,0,40,2,21102,1,442,3,21101,432,0,0,1105,1,475,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,437,438,453,4,0,1001,437,1,437,108,4,437,10,1006,10,469,1102,0,1,437,109,-2,2105,1,0,0,109,4,2102,1,-1,474,1207,-3,0,10,1006,10,492,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,0,1,3,21102,511,1,0,1105,1,516,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,539,2207,-4,-2,10,1006,10,539,21201,-4,0,-4,1106,0,607,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,558,0,0,1106,0,516,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,577,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,599,21201,-1,0,1,21101,0,599,0,105,1,474,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0];
% Extend the memmory "alot"
P = [P, zeros(1,size(P,2)*10)];

% Make 1 computers
I = [P];
i = [1];
irel = [0];
running = [1];
% Omatrix do not support matlab cell arrays, so...
In1 = [];
In2 = [];
In3 = [];
In4 = [];
In5 = [];
Output = [1];

% Make a robot and a black hull to paint
% Directions, 0=up, 1=right, 2=down, 3=left
robotDir = 0;
shipHull = zeros(500,500);
robotPos = [250,250];

for kalle = 0:1

Output = [kalle];
if kalle == 1
  % Reset some random stuff
  shipHull = zeros(100,100);
  robotPos = [50,50];
  shipHull(robotPos(1),robotPos(2))=1;
  running = [1];
  i = [1];
  irel = [0];
end

while running(1)

  for amp = 1:1
  
    if amp == 1
      In1 = [In1 Output];
    elseif amp == 2
      In2 = [In2 Output];
    elseif amp == 3
      In3 = [In3 Output];
    elseif amp == 4
      In4 = [In4 Output];
    else
      In5 = [In5 Output];
    end
  
    Output = [];

    while 1
      oc = mod(I(amp,i(amp)),100);
      ma = mod((I(amp,i(amp))-oc)/100,10);
      mb = mod((I(amp,i(amp))-oc-ma*100)/1000,10);
      mc = mod((I(amp,i(amp))-oc-ma*100-mb*1000)/10000,10);
      if oc == 99
        running(amp) = 0;
        break;

      elseif oc == 1
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if mc == 0
          iUt = I(amp,i(amp)+3)+1;
        elseif mc == 2
          iUt = I(amp,i(amp)+3)+1+irel(amp);
        end
        I(amp,iUt) = a+b;
        step = 4;

      elseif oc == 2
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if mc == 0
          iUt = I(amp,i(amp)+3)+1;
        elseif mc == 2
          iUt = I(amp,i(amp)+3)+1+irel(amp);
        end
        I(amp,iUt) = a*b;
        step = 4;

      elseif oc == 3
        if ma == 0
          iUt = I(amp,i(amp)+1)+1;
        elseif ma == 2
          iUt = I(amp,i(amp)+1)+1+irel(amp);
        end  
        if amp == 1
          if size(In1,2) == 0
            break;
          else
            I(amp,iUt) = In1(1);
            In1 = In1(2:size(In1,2));
          end
        elseif amp == 2
          if size(In2,2) == 0
            break;
          else
            I(amp,iUt) = In2(1);
            In2 = In2(2:size(In2,2));
          end
        elseif amp == 3
          if size(In3,2) == 0
            break;
          else
            I(amp,iUt) = In3(1);
            In3 = In3(2:size(In3,2));
          end
        elseif amp == 4
          if size(In4,2) == 0
            break;
          else
            I(amp,iUt) = In4(1);
            In4 = In4(2:size(In4,2));
          end
        else
          if size(In5,2) == 0
            break;
          else
            I(amp,iUt) = In5(1);
            In5 = In5(2:size(In5,2));
          end
        end
        step = 2;

      elseif oc == 4
        if ma == 0
          Output = [Output I(amp,I(amp,i(amp)+1)+1)];
        elseif ma == 1
          Output = [Output I(amp,i(amp)+1)];
        elseif ma == 2
          Output = [Output I(amp,I(amp,i(amp)+1)+1+irel(amp))];
        end
        step = 2;

      elseif oc == 5
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if a ~= 0
          i(amp) = b+1;
          step = 0;
        else
          step = 3;
        end

      elseif oc == 6
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if a == 0
          i(amp) = b+1;
          step = 0;
        else
          step = 3;
        end

      elseif oc == 7
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if mc == 0
          iUt = I(amp,i(amp)+3)+1;
        elseif mc == 2
          iUt = I(amp,i(amp)+3)+1+irel(amp);
        end
        I(amp,iUt) = a < b;
        step = 4;

      elseif oc == 8
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
        elseif mb == 1
          b = I(amp,i(amp)+2);
        elseif mb == 2
          b = I(amp,I(amp,i(amp)+2)+1+irel(amp));
        end
        if mc == 0
          iUt = I(amp,i(amp)+3)+1;
        elseif mc == 2
          iUt = I(amp,i(amp)+3)+1+irel(amp);
        end
        I(amp,iUt) = a == b;
        step = 4;
      
      elseif oc == 9
        if ma == 0
          a = I(amp, I(amp, i(amp)+1)+1);
        elseif ma == 1
          a = I(amp,i(amp)+1);
        elseif ma == 2
          a = I(amp, I(amp, i(amp)+1)+1+irel(amp));
        end
        irel(amp) = irel(amp)+a;
        step = 2;
      
      end
      i(amp) = i(amp) + step;
    end
  end
  
  % Paint with robot
  if Output(1)==0
    shipHull(robotPos(1),robotPos(2)) = 2;
  elseif Output(1)==1
    shipHull(robotPos(1),robotPos(2)) = 1;
  end
  % Turn
  if Output(2)==0
    robotDir = mod(robotDir-1,4);
  else
    robotDir = mod(robotDir+1,4);
  end
  % Move
  if robotDir == 0
    robotPos = [robotPos(1),robotPos(2)-1];
  elseif robotDir == 1
    robotPos = [robotPos(1)+1,robotPos(2)];
  elseif robotDir == 2
    robotPos = [robotPos(1),robotPos(2)+1];
  else
    robotPos = [robotPos(1)-1,robotPos(2)];
  end
  % Take a picture
  Output = [mod(shipHull(robotPos(1),robotPos(2)),2)];
    
end

sum(sum(shipHull>0))

end

% Print
for i = 1:100
  row = [];
  for j = 1:100
    if shipHull(i,j)==1
      row = [row 'O'];
    else
      row = [row '.'];
    end
  end
  disp(row)
end
