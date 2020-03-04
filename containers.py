from dependency_injector import providers, containers
from board_gateway import BoardGateway
from tic_tac_toe import TicTacToe
from game_end_checker import GameEndChecker

class Configs(containers.DeclarativeContainer):
    # other configs
    pass

class Gateways(containers.DeclarativeContainer):
    board_gateway = providers.Singleton(BoardGateway)
    # other clients 

class UseCases(containers.DeclarativeContainer):
    game_end_checker = providers.Factory(GameEndChecker)
    tic_tac_toe = providers.Factory(TicTacToe, board_gateway=Gateways.board_gateway, game_checker=game_end_checker)
    # other readers