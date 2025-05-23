/*
 * Selling Partner API for Catalog Items
 * Use the Selling Partner API for Catalog Items to retrieve information about items in the Amazon catalog.  For more information, refer to the [Catalog Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/:catalog-items-api-v2022-04-01-use-case-guide).
 *
 * OpenAPI spec version: 2022-04-01
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package software.amazon.spapi.models.catalogitems.v2022_04_01;

import com.google.gson.annotations.SerializedName;
import io.swagger.v3.oas.annotations.media.Schema;
import java.util.Objects;

/** Product type that is associated with the Amazon catalog item, grouped by &#x60;marketplaceId&#x60;. */
@Schema(description = "Product type that is associated with the Amazon catalog item, grouped by `marketplaceId`.")
public class ItemProductTypeByMarketplace {
    @SerializedName("marketplaceId")
    private String marketplaceId = null;

    @SerializedName("productType")
    private String productType = null;

    public ItemProductTypeByMarketplace marketplaceId(String marketplaceId) {
        this.marketplaceId = marketplaceId;
        return this;
    }

    /**
     * Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace
     * IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
     *
     * @return marketplaceId
     */
    @Schema(
            description =
                    "Amazon marketplace identifier. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).")
    public String getMarketplaceId() {
        return marketplaceId;
    }

    public void setMarketplaceId(String marketplaceId) {
        this.marketplaceId = marketplaceId;
    }

    public ItemProductTypeByMarketplace productType(String productType) {
        this.productType = productType;
        return this;
    }

    /**
     * Name of the product type that is associated with the Amazon catalog item.
     *
     * @return productType
     */
    @Schema(
            example = "LUGGAGE",
            description = "Name of the product type that is associated with the Amazon catalog item.")
    public String getProductType() {
        return productType;
    }

    public void setProductType(String productType) {
        this.productType = productType;
    }

    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        ItemProductTypeByMarketplace itemProductTypeByMarketplace = (ItemProductTypeByMarketplace) o;
        return Objects.equals(this.marketplaceId, itemProductTypeByMarketplace.marketplaceId)
                && Objects.equals(this.productType, itemProductTypeByMarketplace.productType);
    }

    @Override
    public int hashCode() {
        return Objects.hash(marketplaceId, productType);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class ItemProductTypeByMarketplace {\n");

        sb.append("    marketplaceId: ").append(toIndentedString(marketplaceId)).append("\n");
        sb.append("    productType: ").append(toIndentedString(productType)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /** Convert the given object to string with each line indented by 4 spaces (except the first line). */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }
}
