tic
C = [];
for i = 1:6
  for j = i:9
    if (i*10+j <= 66)
      for k = j:9
        if (i*100+j*10+k >= 178)
          a = i==j & j~=k;
          for l = k:9
            b = i~=j & j==k & k~=l;
            for m = l:9
              c = j~=k & k==l & l~=m;
              for n = m:9
                d = k~=l & l==m & m~=n;
                e = m == n & l~=m;
                if (a|b|c|d|e)
                  C = [C; [i j k l m n]];
               end
              end
            end
          end
        end
      end
    end
  end
end
toc
