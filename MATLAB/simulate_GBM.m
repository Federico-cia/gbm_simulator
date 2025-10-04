%num_days=input("Inserisci numero di giorni di previsione: ");
%sigma=input("Inserisci volatilità/deviazione standard: ");
%mu=input("Inserisci rendimento atteso/drift: ");
%initial_price=input("Prezzo iniziale di bitcoin: ");
%num_simulations=input("Inserisci numero di simulazioni (linee del grafico): ");



num_days=30;
%sigma=0.2501342278057532;
%mu=0.0042266598729455455;     mu = 1.54249   
sigma= 2.868315;
%mu=0.7910718;
mu=1.54249;
initial_price=95000;
num_simulations=30;

simulate_GBM(num_days, sigma, mu, initial_price,num_simulations)




%___________________________________________________________________________________

function simulate_GBM(num_days, sigma, mu, initial_price, num_simulations)
    
    % Time vector: from day 0 to num_days, each time step is 1 day
    t = 0:num_days;

    % Initialize figure for plotting
    figure;
    hold on;
    xlabel('Days');
    ylabel('Bitcoin Price');
    %title('Geometrical Brownian Motion - Bitcoin Price Simulation');

    for i = 1:num_simulations
        % Generate a random walk for GBM: dS = mu*dt + sigma*sqrt(dt)*Z
        Z = randn(1, num_days);

        S = zeros(1, num_days+1);
        S(1) = initial_price;
        disp(Z)
        for j = 2:num_days+1
            S(j) = S(j-1) * exp((mu - 0.5*sigma^2)/365 + sigma*Z(j-1)/sqrt(365));
        end

        plot(t, S, 'LineWidth', 0.9);
    end
    
    

    %linea di tendenza del moto browniano
    K=zeros(1, num_days+1);
    K(1)=initial_price;
    for i=2:num_days+1
        %K(i)=K(i-1)*exp((mu-0.5*sigma^2)/num_days);
        K(i)=K(i-1)*exp((mu)/365);
    end
    plot(t,K,'color','k','Linewidth',1.7)

    %ylim([87000,130000])

    hold off;
    grid on;
end
