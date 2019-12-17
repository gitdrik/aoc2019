P = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99];

maxthrust = 0;

apas = [5 6 7 8 9];

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


% Make 5 computers
I = [P;P;P;P;P];
i = [1;1;1;1;1];
running = [1;1;1;1;1];
% Omatrix do not support cell arrays, so
In1 = [pha 0];
In2 = [phb];
In3 = [phc];
In4 = [phd];
In5 = [phe];
Output = [];

while running(5)

for amp = 1:5

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
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      iUt = I(amp,i(amp)+3)+1;
      I(amp,iUt) = a+b;
      step = 4;

    elseif oc == 2
      if ma == 0
          a = I(amp,I(amp,i(amp)+1)+1);
      elseif ma == 1
          a = I(amp,i(amp)+1);
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      iUt = I(amp,i(amp)+3)+1;
      I(amp,iUt) = a*b;
      step = 4;

    elseif oc == 3
      iUt = I(amp,i(amp)+1)+1;
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
      end
      step = 2;

    elseif oc == 5
      if ma == 0
          a = I(amp,I(amp,i(amp)+1)+1);
      elseif ma == 1
          a = I(amp,i(amp)+1);
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      if a ~= 0
        i(amp) = b+1;
        step = 0;
      else
        step = 3;
      end

    elseif oc == 6
      if ma == 0
          a = I(amp,I(amp,i(amp)+1)+1);
      elseif ma == 1
          a = I(amp,i(amp)+1);
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      if a == 0
        i(amp) = b+1;
        step = 0;
      else
        step = 3;
      end

    elseif oc == 7
      if ma == 0
          a = I(amp,I(amp,i(amp)+1)+1);
      elseif ma == 1
          a = I(amp,i(amp)+1);
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      iUt = I(amp,i(amp)+3)+1;
      I(amp,iUt) = a < b;
      step = 4;

    elseif oc == 8
      if ma == 0
          a = I(amp,I(amp,i(amp)+1)+1);
      elseif ma == 1
          a = I(amp,i(amp)+1);
      end
      if mb == 0
          b = I(amp,I(amp,i(amp)+2)+1);
      elseif mb == 1
          b = I(amp,i(amp)+2);
      end
      iUt = I(amp,i(amp)+3)+1;
      I(amp,iUt) = a == b;
      step = 4;

    end
    i(amp) = i(amp) + step;
  end
end
end

maxthrust = max(maxthrust, Output(1));
end
end
end
maxthrust
end
