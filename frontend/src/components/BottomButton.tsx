import { FC } from "react";
import { ActionIcon } from "@mantine/core";
import { BiPlus } from "react-icons/bi";

interface IBottomButton {
    onClick: () => void;
}

const BottomButton: FC<IBottomButton> = ({ onClick }) => {
    return (
        <ActionIcon
            size="xl"
            pos="fixed"
            bottom={10}
            right={10}
            onClick={onClick}
            style={{
                borderRadius: "50%",
                width: "60px",
                height: "60px",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            <BiPlus size={36} />
        </ActionIcon>
    );
};

export default BottomButton;
