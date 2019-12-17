P = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99];

maxthrust = 0;

apas = [0 1 2 3 4];

for apa = 1:5
  pha = apas(apa);
  bepas = [apas(1:(apa-1)) apas((apa+1):5)];
  for bepa = 1:4
    phb = bepas(bepa);
    cepas = [bepas(1:(bepa-1)) bepas((bepa+1):4)];
    for cepa = 1:3
      phc = cepas(cepa);
      depas = [cepas(1:(cepa-1)) cepas((cepa+1):3)];
      for depa = 1:2
        phd = depas(depa);
        if depa == 1
           phe = depas(2);
        else
           phe = depas(1);
        end

phase = [pha phb phc phd phe]
Output = [0];

for amp = 1:5

  I=P;
  i = 1;
  Input = [phase(amp) Output(1)];
  Output = [];

  while 1
    oc = mod(I(i),100);
    ma = mod((I(i)-oc)/100,10);
    mb = mod((I(i)-oc-ma*100)/1000,10);
    mc = mod((I(i)-oc-ma*100-mb*1000)/10000,10);
    if oc == 99
      break;

    elseif oc == 1
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      iUt = I(i+3)+1;
      I(iUt) = a+b;
      step = 4;

    elseif oc == 2
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      iUt = I(i+3)+1;
      I(iUt) = a*b;
      step = 4;

    elseif oc == 3
      iUt = I(i+1)+1;
      I(iUt) = Input(1);
      Input = Input(2:size(Input,2));
      step = 2;

    elseif oc == 4
      if ma == 0
          Output = [I(I(i+1)+1) Output];
      elseif ma == 1
          Output = [I(i+1) Output];
      end
      step = 2;

    elseif oc == 5
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      if a ~= 0
        i = b+1;
        step = 0;
      else
        step = 3;
      end

    elseif oc == 6
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      if a == 0
        i = b+1;
        step = 0;
      else
        step = 3;
      end

    elseif oc == 7
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      iUt = I(i+3)+1;
      I(iUt) = a < b;
      step = 4;

    elseif oc == 8
      if ma == 0
          a = I(I(i+1)+1);
      elseif ma == 1
          a = I(i+1);
      end
      if mb == 0
          b = I(I(i+2)+1);
      elseif mb == 1
          b = I(i+2);
      end
      iUt = I(i+3)+1;
      I(iUt) = a == b;
      step = 4;

    end
    i = i + step;
  end
  
end

maxthrust = max(maxthrust, Output(1));

end
end
end
maxthrust
end
